import os
import codecs
import shutil
import html

# path to your music folder
path = 'Y:/音乐'

"""
Fixes the encoding of file
"""
def fix(filename, replace=False):
    try:
        content = ""
        with codecs.open(filename, "r", "gbk") as f:
            lines = f.readlines()
            for line_num, line in enumerate(lines):
                if line_num >= 5:
                    content += (line[:10] + html.unescape(line[10:-1])).replace('\n','') + "\n"
                else:
                    content += html.unescape(line)

        with codecs.open(filename if replace else f"fixed_{filename}", "w", "utf-8") as f:
            f.write(content)
        return True
    except:
        # print(f"Error processing {filename}")
        return False

"""
Finds and fixes the encoding of all files in a directory (default lrc files)
"""
def fix_dir(path, replace=False, filetype=".lrc"):
    files = [
        val for sublist in [
            [
                os.path.join(i[0], f) for f in i[2] if f.endswith(filetype)
            ] for i in os.walk(path)
        ] for val in sublist
    ]
    print(f"Fixed {sum(fix(file, replace) for file in files)} files")

"""
Moves all files in a directory to the parent directory
"""
def move_dir(subdir):
    success = 0
    failed = 0
    for filename in os.listdir(subdir):
        try:
            shutil.move(f"{subdir}/{filename}", f"{subdir}/../{filename}")
            success += 1
        except:
            failed += 1
            # print(f"Error moving {filename}")
    print(f"Moved {success} files ({failed} failed)")
    
if __name__ == "__main__":
    # Example usage
    fix("雨爱.lrc")
    move_dir(f"{path}/VipSongsDownload")
    fix_dir(path, True)
    print("Done")
