import sys
txtfile = "unicode_table.txt"
print("creating file: " + txtfile)
F = open(txtfile, "w", encoding="utf-16", errors='ignore')
for uc in range(sys.maxunicode):
    line = "%s %s" % (hex(uc), chr(uc))
    print(line, file=F)
F.close()