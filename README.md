# maya-thinclient

Collection of info and scripts on how to create thinclient installs of Maya on a single machine. This gives side by side "installs" of Maya without actually installing anything on the machine and every "install" is completely independant from the others.

On linux: a collection of scripts that will take a tgz file and unpack it in the current folder, to run it you execute a startup script that sets the required environment variables and starts Maya.

On Windows: a batch script that configures Maya to run from a specific set of folders. Maya doesn't get installed on the machine, instead a donor machine is used and files are copied across (or could be placed on a network drive so that multiple artists can access them).

Oh and I've also included some examples for 3ds Max and Motion Builder in the Windows folder.
