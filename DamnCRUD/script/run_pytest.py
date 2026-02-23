#!/usr/bin/env python3
"""
Helper script to run DamnCRUD tests with various configurations
"""
import sys
import subprocess
import argparse


def run_command(cmd, description):
    """Execute a command and print results"""
    print(f"\n{'='*60}")
    print(f"📋 {description}")
    print(f"{'='*60}")
    print(f"Command: {' '.join(cmd)}\n")
    
    result = subprocess.run(cmd, shell=False)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Run DamnCRUD Selenium tests")
    parser.add_argument(
        "--mode",
        choices=["all", "parallel", "search", "crud", "validation", "report"],
        default="all",
        help="Test execution mode"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=0,
        help="Number of parallel workers (0 = auto)"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    # Base pytest command
    base_cmd = ["pytest"]
    
    if args.verbose:
        base_cmd.append("-v")
    
    # Mode-specific configurations
    if args.mode == "all":
        cmd = base_cmd.copy()
        return run_command(cmd, "Running all tests")
    
    elif args.mode == "parallel":
        workers = "auto" if args.workers == 0 else str(args.workers)
        cmd = base_cmd + ["-n", workers]
        return run_command(cmd, f"Running tests in parallel with {workers} workers")
    
    elif args.mode == "search":
        cmd = base_cmd + ["-m", "search"]
        return run_command(cmd, "Running search tests only")
    
    elif args.mode == "crud":
        cmd = base_cmd + ["-m", "crud"]
        return run_command(cmd, "Running CRUD tests only")
    
    elif args.mode == "validation":
        cmd = base_cmd + ["-m", "validation"]
        return run_command(cmd, "Running validation tests only")
    
    elif args.mode == "report":
        cmd = base_cmd + [
            "-n", "auto",
            "--html=report.html",
            "--self-contained-html"
        ]
        result = run_command(cmd, "Running tests with HTML report generation")
        if result == 0:
            print("\n✅ Test report generated: report.html")
        return result


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⚠️  Test execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
