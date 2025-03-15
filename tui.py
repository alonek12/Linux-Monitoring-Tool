import time
import psutil
from rich.console import Console
from rich.table import Table
from rich.live import Live

def get_system_stats():
    table = Table(title="System Monitor")
    
    table.add_column("Metric", justify="left", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="magenta")
    
    cpu_usage = psutil.cpu_percent(interval=None, percpu=True)
    cpu_text = " | ".join([f"Core {i}: {usage}%" for i, usage in enumerate(cpu_usage)])
    
    table.add_row("CPU Usage", cpu_text)
    table.add_row("Memory Usage", f"{psutil.virtual_memory().percent}%")
    table.add_row("Swap Usage", f"{psutil.swap_memory().percent}%")
    table.add_row("Disk Usage", f"{psutil.disk_usage('/').percent}%")
    
    net_io = psutil.net_io_counters()
    table.add_row("Network (Sent / Recv)", f"{net_io.bytes_sent / 1e6:.2f} MB / {net_io.bytes_recv / 1e6:.2f} MB")
    
    return table

def main():
    console = Console()
    with Live(get_system_stats(), console=console, refresh_per_second=1) as live:
        while True:
            live.update(get_system_stats())
            time.sleep(1)

if __name__ == "__main__":
    main()
