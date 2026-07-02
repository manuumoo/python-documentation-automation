import csv
from pathlib import Path
from datetime import datetime


DATA_FILE = Path("data/processes.csv")
OUTPUT_FILE = Path("output/process_documentation_report.md")


def read_processes(file_path):
    """Read process information from a CSV file."""
    processes = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            processes.append(row)

    return processes


def generate_markdown_report(processes):
    """Generate a Markdown documentation report from process data."""
    report_date = datetime.now().strftime("%Y-%m-%d")

    lines = []
    lines.append("# Process Documentation Report")
    lines.append("")
    lines.append(f"Generated on: {report_date}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"Total processes reviewed: {len(processes)}")
    lines.append("")

    high_priority = [
        process for process in processes
        if process["priority"].lower() == "high"
    ]

    lines.append(f"High priority processes: {len(high_priority)}")
    lines.append("")
    lines.append("## Process Details")
    lines.append("")

    for process in processes:
        lines.append(f"### {process['process_name']}")
        lines.append("")
        lines.append(f"- **Owner:** {process['owner']}")
        lines.append(f"- **Status:** {process['status']}")
        lines.append(f"- **Last Update:** {process['last_update']}")
        lines.append(f"- **Priority:** {process['priority']}")
        lines.append(f"- **Notes:** {process['notes']}")
        lines.append("")

    lines.append("## Recommendations")
    lines.append("")
    lines.append("- Review high priority processes first.")
    lines.append("- Keep documentation updated after every process change.")
    lines.append("- Use automation to reduce repetitive documentation tasks.")
    lines.append("- Track process status regularly to improve visibility.")
    lines.append("")

    return "\n".join(lines)


def save_report(content, output_file):
    """Save the Markdown report into the output folder."""
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, mode="w", encoding="utf-8") as file:
        file.write(content)


def main():
    if not DATA_FILE.exists():
        print(f"Error: The file {DATA_FILE} was not found.")
        return

    processes = read_processes(DATA_FILE)
    report = generate_markdown_report(processes)
    save_report(report, OUTPUT_FILE)

    print(f"Report generated successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
