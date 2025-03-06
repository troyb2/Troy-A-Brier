from PyPDF2 import PdfMerger
import argparse
import glob


parser = argparse.ArgumentParser(description="Quick PDF Merger")

parser.add_argument('-d', '--in_dir')   
parser.add_argument('-o', '--out_file')

args = parser.parse_args()

outfile = args.out_file

print('#####################################################################')
print(outfile)
print(args.in_dir)
print('#####################################################################')

#file_list = glob.glob(str(args.in_dir)+'*')
if str(args.in_dir)=='cv':
    file_list = ['letter.pdf','cv.pdf']
elif str(args.in_dir)=='resume':
    file_list = ['letter.pdf','resume.pdf']
else:
    print('NEED TO DEFINE CV OR RESUME')
    file_list=[]

merger = PdfMerger()

for f in file_list:
	print('adding',f)
	#Merge Individual PDF files
	merger.append(f)
#	print('adding','norm-'+f)
#	merger.append('norm-'+f)

merger.write(outfile)
merger.close()
print("Generated "+outfile)
