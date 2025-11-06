#!/usr/bin/env python3
"""
Professional-ish port scan helper using python-nmap.

Usage:
    python scan.py 192.168.100.12 --ports 22-443 --verbose
"""

from __future__ import annotations
import argparse
import logging
import platform
import shutil
import subprocess
from typing import Dict, List, Any, Optional
import nmap
import tabulate as tb
# python-nmap package (wraps the nmap binary)


logger = logging.getLogger(__name__)


def is_host_up(target: str, count: int = 2, timeout: int = 2) -> bool:
    """
    Ping a host to check if it is reachable.

    Uses the system ping utility via subprocess; avoids os.system hacks.
    Returns True if the host responds.
    """
    ping_cmd = "ping"
    if shutil.which(ping_cmd) is None:
        logger.debug("ping utility not found on PATH — assuming host unknown.")
        return False

    system = platform.system().lower()
    if system == "windows":
        args = [ping_cmd, "-n", str(count), "-w", str(timeout * 1000), target]
    else:
        args = [ping_cmd, "-c", str(count), "-W", str(timeout), target]

    try:
        res = subprocess.run(
            args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False
        )
        return res.returncode == 0
    except Exception as exc:
        logger.exception("Error running ping: %s", exc)
        return False


def run_nmap_scan(
    target: str, ports: str = "1-1024", arguments: str = "-sV"
) -> List[Dict[str, Any]]:
    """
    Run nmap scan on `target` and return structured results.

    Returns a list (one element per host) of dicts:
    [{
        "ip": "x.x.x.x",
        "hostname": "name",
        "state": "up",
        "ports": [{"port": 22, "protocol": "tcp", "state": "open", "service": "ssh", "product": "OpenSSH"}...]
    }]
    """
    if shutil.which("nmap") is None:
        raise RuntimeError("nmap binary not found on PATH. Please install nmap.")

    scanner = nmap.PortScanner()
    # Example: nm.scan(hosts="192.168.1.0/24", ports="22-443", arguments="-sV -T4")
    scanner.scan(hosts=target, ports=ports, arguments=arguments)

    results: List[Dict[str, Any]] = []
    for host in scanner.all_hosts():
        host_info: Dict[str, Any] = {
            "ip": host,
            "hostname": scanner[host].hostname(),
            "state": scanner[host].state(),
            "ports": [],
        }
        for proto in scanner[host].all_protocols():
            ports_list = sorted(scanner[host][proto].keys())
            for p in ports_list:
                port_data = scanner[host][proto][p]
                host_info["ports"].append(
                    {
                        "port": int(p),
                        "protocol": proto,
                        "state": port_data.get("state"),
                        "service": port_data.get("name"),
                        "product": port_data.get("product"),
                        "version": port_data.get("version"),
                    }
                )
        results.append(host_info)
    return results


def scan_target(
    target: str, ports: str, arguments: str, ping_first: bool = True
) -> Optional[List[Dict[str, Any]]]:
    """
    High-level function: optionally ping, then run nmap and return structured results.
    Returns None if host unreachable (and ping_first=True).
    """
    if ping_first:
        if not is_host_up(target):
            logger.info("Host %s did not respond to ping — skipping scan.", target)
            return None
    try:
        return run_nmap_scan(target=target, ports=ports, arguments=arguments)
    except Exception:
        logger.exception("Nmap scan failed.")
        raise


if __name__ == "__main__":
    table = scan_target("192.168.100.12", ports="22-1024", arguments="-sV")
    print(tb(table))
