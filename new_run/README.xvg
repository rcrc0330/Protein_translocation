# Protein_translocation
## How to run a new protein file (The codes and paths correspond to the folder "new_run")
1. Have the pdb file (protein.pdb) - To run a new file all you need is a pdb file of the protein you want to run the code on
2. Place the protein.pdb file in the "martini" folder and run the following command in cmd/conda prompt (python 3 is necessary for this version of martinizer):
  ```bash
  python martinizer.py -f protein.pdb -o protein.top -x protein-CG.pdb -ff martini22
  ```
This script will generate the necessary CG pdb file (protein-CG.pdb) and the corresponding itp file (probably protein.itp, if not change it to protein.itp).

3. Use gromacs editconf (or anything else you want to) to place the protein-CG.pdb in such a way that the first bead is just inside the mouth of the pore (the center of pore is at {0,0,0} so mouth would be {0,0,negative of half pore length})
  ```bash
  gmx_mpi editconf -f protein-CG.pdb -o changed.pdb -center x y z
  ```
  Change the 3 coordinates (x,y,z) appropriately until first bead is where you need it to be. (The output now is the modified protein-CG.pdb)

4. Place the modified protein-CG.pdb and protein.itp in "push" folder and run the protein gro2lam.ipynb, this will create the required lammps datafile (data.txt)
5.   run protein_push.in after changing the region push inside the script appropriately (if should be just outside the mouth of the pore):
  ```bash
  lmp -in protein_push.in
  ```
This will push all the beads outside the pore region apart from the first bead which will be stationary inside the pore mouth. Load the output.lammpstrj in vmd and save the last frame in temp.pdb

6. Place temp.pdb in "gen_init" folder and run data_file_creator.ipynb and give the Length and breath of the pore wall, the depth of the pore, the diameter of the pore hole, the diameter of beads used to create pore walls, and the diameter of beads used to create pore cylinder in the respective order. This will create the lammps data file(data_file.txt)

7. run protein_get_init.in:
  ```bash
  lmp -in protein_get_init.in
  ```
8. load the output.lammpstrj in vmd and save the first frame as first.pdb in the same folder. Now run gen_initial_pro.ipynb and you will get the 100 frames needed for the initial conformations in "init_csv_fin"

9. Now run the init_csv_to_data_merged.ipynb and you will get the 100 lammps data files corresponding to the 100 initial conformations in "init_conf_fin"

10. Place the "init_conf_fin" into "Final_run" and edit second.txt to define region appropraitely (if you change pore depth) and edit forth.txt if you want to edit the electric field. Also, edit trans_time.py so that n_chain has represents the number of beads in the protein(make n_chain = 236 if 236 beads in protein). Now put this "Final_run" folder on cluster and run_short.slurm. The result.txt would contain the corresponding time of translocation for each conformation at the end of the job. Negative translocation time indicates a failed translocation.
  ```bash
  sbatch run_short.slurm
  ```
