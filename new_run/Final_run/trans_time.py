import mdtraj as md
import sys

ent = -50/10
exit = 0/10
nchain = 236
timestep = 3
Nsteps = 50000
print(sys.argv[1])
f = md.load_lammpstrj("output/output" + sys.argv[1] + ".lammpstrj",top = "first.pdb")

hi = f.n_frames-1
inn = -1
for i in range(f.n_frames):
    pos = f.xyz[i][0][2]
    for j in range(0,nchain):
        pos = max(pos,f.xyz[i][j][2])
    if(pos>ent):
        if(inn==-1):
            inn = i
    else:
        inn=-1

out = -1
for i in range(f.n_frames):
    pos = f.xyz[i][0][2]
    for j in range(0,nchain):
        pos = min(pos,f.xyz[i][j][2])
    if(pos>exit):
        if(out==-1):
            out = i
    else:
        out=-1

time = (timestep * Nsteps)/1000000000
file = open("result.txt","a")
if(sys.argv[1]=="1"):
    file.write("\n\n-------\n\n")
file.write(sys.argv[1] + " inn " + str(inn) + " out " + str(out) + " time in us " + str((out-inn)*time)  + "\n")



