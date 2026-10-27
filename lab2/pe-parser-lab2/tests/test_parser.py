"""Usage: python tests/test_parser.py PATH_TO_PARSER PATH_TO_LAB2_SAMPLES"""
import pathlib
import subprocess
import sys

exe = pathlib.Path(sys.argv[1]).resolve()
samples = pathlib.Path(sys.argv[2]).resolve()
fail = 0
for group in ('valid', 'malformed'):
    for file in sorted((samples / group).glob('*')):
        run = subprocess.run([str(exe), file.name], cwd=file.parent,
                             capture_output=True, text=True, timeout=10)
        reference = (samples / 'expected' / (file.name + '.txt')).read_text()
        actual = run.stdout + run.stderr
        if group == 'valid' or file.name in ('ep_outside.exe', 'wx_section.exe'):
            ok = run.returncode == 0 and actual == reference
        else:
            ok = run.returncode != 0 and 'error:' in run.stderr
        print(('PASS' if ok else 'FAIL'), file.name)
        fail += not ok
sys.exit(bool(fail))
