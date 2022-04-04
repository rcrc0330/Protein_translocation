import mdtraj as md

ent = -10/10
exit = 10/10
nchain = 100

f = md.load_lammpstrj("lamp2/output.lammpstrj",top = "hola.pdb")

hi = f.n_frames-1
lo = 0
inn = -1
while(lo<hi):
    mid = int((lo+hi)/2)
    pos = f.xyz[int(mid)][f.n_atoms-1][2]
    for i in range(f.n_atoms-nchain,f.n_atoms):
        pos = max(pos,f.xyz[int(mid)][i][2])
    if(pos>ent):
        hi = mid
    else:
        lo = mid+1
if(lo==f.n_frames):
    print("NA")
else:
    inn = hi

hi = f.n_frames-1
lo = 0
out = -1
while(lo<hi):
    mid = int((lo+hi)/2)
    pos = f.xyz[int(mid)][f.n_atoms-1][2]
    for i in range(f.n_atoms-nchain,f.n_atoms):
        pos = min(pos,f.xyz[int(mid)][i][2])
    if(pos>exit):
        hi = mid
    else:
        lo = mid+1
if(lo==f.n_frames):
    print("The polymer didn't enter")
else:
    out = hi


time = (out-inn)*50*0.005

file = open("result.txt",a)

file.write(time)



