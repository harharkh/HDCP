# HDCP
This is a database that contains the critical configurations of hard disks on the hexagonal torus, where the number of hard disks is $n = 2 \ldots 12$. A critical configuration is one where disk contacts prevent any collective motion that would allow the radius of all disks to increase linearly with the extent of the motion. Equivalently, a critical configuration is one that has a mechanically-balanced contact graph. The torus is the regular hexagon of edge length $1 / \sqrt{3}$ with opposite edges identified.

## **Security Statement**
Connecting to a Jupyter notebook server running on your local machine can provide many benefits. With these benefits come serious potential risks. By connecting to a local runtime, you are allowing the Colaboratory frontend to execute code in the notebook using the local resources on your machine. This means that the notebook could:

- Invoke arbitrary commands (e.g. "rm -rf /")
- Access the local file system
- Run malicious content on your machine

Before attempting to connect to a local runtime, make sure you trust the authors of the notebook and ensure you understand what code is being executed. For more information on the Jupyter notebook server's security model, consult [Jupyter's documentation](https://jupyter-notebook.readthedocs.io/en/stable/security.html).

## **Usage**
FIX ME The usage of this notebook is straightforward. The first cell after this section imports the necessary datafiles and libraries. The second cell calls the desired datafile. The critical points database is available for $n=2 \ldots 12$. You can choose which database you want to load. You can also use the filter option to analyze the critical points. After you load the first two cells, the plotting is done in the third cell. All you have to do is to select the critical point you want to plot from the table from the previous cell. The last cell also prints the adjacency matrix of the critical points.

Suppose we want to plot the 4th critical point of $n=7$ case.
- Change the value of _filename_ as _filename = 'hard_disks/7disk.csv'_; 
- Change the value of _which_crit_ as _which_crit = 4;_

## **References**
Research into the topology of the configuration space of hard disks is ongoing, but the references below provide some context for this project.

- G. Carlsson, J. Gorham, M. Kahle, J. Mason, [Computational topology for configuration spaces of hard disks](https://doi.org/10.1103/PhysRevE.85.011303), Phys. Rev. E 85 (2012): 011303.
- Y. Baryshnikov, P. Bubenik, M. Kahle, [Min-type Morse theory for configuration spaces of hard spheres](https://doi.org/10.1093/imrn/rnt012), International Mathematics Research Notices 2014.9 (2014): 2577–2592.
- H. Alpert, M. Kahle, R. MacPherson, [Configuration spaces of disks in an infinite strip](https://arxiv.org/abs/1908.04241), arXiv:1908.04241.

## **Contributors**
The contributors to this project are (by alphabetical order of last name):

- Ozan Ericok (oericok@ucdavis.edu)
- Matthew Kahle (kahle.70@osu.edu)
- Jeremy Mason (jkmason@ucdavis.edu)
- Katherine Ritchey (ritcheka@mountunion.edu)

Please contact Matthew Kahle (kahle.70@osu.edu) or Jeremy Mason (jkmason@ucdavis.edu) for more information.

## **License**
The contents of this repository are licenced under the [GNU General Public License, Version 3](https://www.gnu.org/licenses/gpl-3.0.en.html).

## **Acknowledgements**
This material is based upon work supported by the National Science Foundation under Grant No. 1839370. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
