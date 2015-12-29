import deletefile.delete_path_all_txtfile
import deletefile.delete_path_all_xlsfile

def DelXlsAndTxt(dirpaths):
    deletefile.delete_path_all_txtfile.deltxtfilemain(dirpaths)
    deletefile.delete_path_all_xlsfile.delxlsfilemain(dirpaths)
