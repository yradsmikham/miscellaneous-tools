import shutil, random, os

dirpath="/Users/yvonneradsmikham/Microsoft/fox-audio/wav/gunshot_other_complete_tfrecord"
destpath="/Users/yvonneradsmikham/Microsoft/fox-audio/wav/gunshot_other_training_60"
other_destpath="/Users/yvonneradsmikham/Microsoft/fox-audio/wav/gunshot_other_test_40"
filenames = random.sample(os.listdir(dirpath), 600)
all_files = os.listdir(dirpath)
for fname in filenames:
    srcpath = os.path.join(dirpath, fname)
    dest= os.path.join(destpath, fname)
    shutil.copyfile(srcpath, dest)

# for filename in all_files:
#     for fname in filenames:
#         if filename == fname:
#             #print("In Training Set")
#             continue
#         else:
#             source = os.path.join(dirpath, filename)
#             destination = os.path.join(other_destpath, filename)
#             shutil.copyfile(source, destination)

for filename in all_files:
    if os.path.exists(os.path.join(destpath, filename)):
        continue
    else:
        source = os.path.join(dirpath, filename)
        destination = os.path.join(other_destpath, filename)
        shutil.copyfile(source, destination)
