import sys
import fileinput 
import gzip


def split_compressed_file(filename, chunk_size):
	
	fout = None
	headers = None
	files = []
	with gzip.open(filename, 'rb') as data:
		headers = next(data)
		print headers
		for i, line in enumerate(data):
			if i % chunk_size == 0:
			    if fout: fout.close()
			    fout = open('output%d.txt' % (i/chunk_size), 'wb')
			    fout.write(headers)
			fout.write(line)
		files.append(fout)
		fout.close()

	return headers, files

def split_file(filename, chunk_size):
	
	fout = None
	headers = None
	with open(filename, 'rb') as data:
		headers = next(data)
		print headers
		for i, line in enumerate(data):
			if i % chunk_size == 0:
				if fout: fout.close()
				fout = open('output%d.txt' % (i/chunk_size), 'wb')
				fout.write(headers)
			fout.write(line)

		fout.close()

if __name__ == '__main__':

	filename = sys.argv[1]
	chunk_size = int(sys.argv[2])
	split_compressed_file(filename, chunk_size)
