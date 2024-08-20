# chemprop_atomvalence
Scan dataset to avoid chemprop AtomValenceException
Errors may occur when using "--split_type" flag with "scaffold_balanced" option.
e.g. "rdkit.Chem.rdchem.AtomValenceException: Explicit valence for atom # 8 C greater than permitted"
########################################################
As Chemprop will not return where the erroneous moleulces exist and it will exit smoothly without any error that can be captured, a script is written to scan the training dataset and drop the incorrect valence molecules so that molecular core option can be used with ease.
The script split the whole training dataset into 2 mol/set so that Chemprop training on each two molecules can localize and detect real-time errors with all the output written to log file.
"--split_size" is set as 0.5 0.5 0 as one molecule acts as training and the other acts as validation.
########################################################
After running through all the molecules in training dataset, the following command is used to localize AtomValenceException:
## grep -i "Valence" *.log
Then, it is recommended to visualize erroneous molecular SMILES in order to determine which one of the two is actually incorrect.

P.s. The program is running on Windows system and the corresponding flag should be checked if necessary.
P.s. Molecules that cannot be kekulized will not terminate Chemprop_train program
