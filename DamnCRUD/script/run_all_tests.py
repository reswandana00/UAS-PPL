import subprocess
import os
import time
from datetime import datetime

test_scripts = [
    "tc_005_search_kontak.py",
    "tc_006_tambah_kontak_valid.py",
    "tc_007_validasi_field_kosong.py",
    "tc_008_update_kontak.py",
    "tc_009_delete_kontak.py"
]

def run_test(script_name):
    print(f"\n{'='*70}")
    print(f"Menjalankan: {script_name}")
    print(f"{'='*70}\n")
    
    try:
        result = subprocess.run(
            ["python", script_name],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        print(result.stdout)
        
        if result.stderr:
            print(f"STDERR: {result.stderr}")
        
        return result.returncode == 0
    
    except Exception as e:
        print(f"ERROR menjalankan {script_name}: {str(e)}")
        return False

def main():
    start_time = datetime.now()
    
    print(f"\n{'#'*70}")
    print(f"# AUTOMATION TEST - DamnCRUD")
    print(f"# Waktu mulai: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"# Total test: {len(test_scripts)}")
    print(f"{'#'*70}\n")
    
    results = {}
    
    for script in test_scripts:
        success = run_test(script)
        results[script] = "PASS" if success else "FAIL"
        time.sleep(2)
    
    end_time = datetime.now()
    duration = end_time - start_time
    
    print(f"\n{'='*70}")
    print(f"SUMMARY TEST RESULTS")
    print(f"{'='*70}")
    
    passed = sum(1 for result in results.values() if result == "PASS")
    failed = sum(1 for result in results.values() if result == "FAIL")
    
    print(f"\n{'Test Case':<40} {'Status':>10}")
    print(f"{'-'*50}")
    
    for script, status in results.items():
        status_symbol = "✓" if status == "PASS" else "✗"
        print(f"{script:<40} {status_symbol} {status:>8}")
    
    print(f"\n{'-'*50}")
    print(f"Total: {len(test_scripts)} | Passed: {passed} | Failed: {failed}")
    print(f"Duration: {duration.total_seconds():.2f} seconds")
    print(f"{'='*70}\n")

if __name__ == "__main__":
    main()
