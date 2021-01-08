# flxfs 

flxfs is a portable personal filesystem designed to
facilitate file organization in ways that traditional file
systems can't.

## Architecture

flxfs operates as an additional layer on top of existing
filesystems, rather than implementing low-level functionality.

In flxfs, all files are stored under a single directory;
their name under that directory is a hash of their contents. 
All file metadata is stored in a sqlite database.

## Features

### Portability

By operating on top of existing filesystems as a client, a
flxfs filesystem can be compressed, transported, and replicated
across computers with ease.

### Tagging

Tagging is an incredibly powerful tool for organization, and yet,
tagging, as implemented by modern file systems, is not portable.
If one frequently uses a variety of computers, this is reason
enough to eschew tags.

### Error Detection

Storage media experience bit flips at alarming rates. Storing
files under their hash offers basic mitigation of corruption
at rest.

### Abstracting Hierarchy

Have you ever wished you could store the same file under more
than one directory? Or, have you ever wished you could
auto-generate a directory based on the attributes of a file (say,
a folder of pictures organized by year, month, and day?)

flxfs frees files from the cage of location, allowing the creation
of multiple lenses and collections on top of its filestore. 

### Power

flxfs is native to a command-line interface, but can also check
working copies of its hierarchies in and out, allowing powers
users to navigate their files in the way that best suits the
situation.
