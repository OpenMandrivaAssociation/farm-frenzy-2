/* Wrapper to launch a wine based game setgid games                     */
/* (c) 2013 Bernhard Rosenkraenzer <bero@lindev.ch>                     */
/* Released under the terms of the GNU General Public License (GPL) v3. */
#include <stdlib.h>
#include <sys/types.h>
#include <grp.h>
#include <stdio.h>
#include <unistd.h>
#include <assert.h>

#ifndef GAMEPATH
#error Compile with -DGAMEROOT=\"/path/to/wineenv\" -DGAMEPATH=\"/path/to/game/files\"
#endif

#ifndef GAME
#define GAME "game.exe"
#endif

int main(int argc, char **argv) {
	struct group *g = getgrnam("games");
	if(!g || !g->gr_gid) {
		fprintf(stderr, "Group games doesn't exist\n");
		exit(1);
	}
#ifdef GAMEROOT
	chown(GAMEROOT, getuid(), g->gr_gid);
	chown(GAMEROOT "/dosdevices", getuid(), g->gr_gid);
	chown(GAMEROOT "/drive_c", getuid(), g->gr_gid);
#endif
	chown(GAMEPATH, getuid(), g->gr_gid);
	setregid(g->gr_gid, g->gr_gid);
	setreuid(getuid(), getuid());
	if(!getuid() || !geteuid() || !getgid() || !getegid()) {
		fprintf(stderr, "Don't play games as root\n");
		exit(2);
	}
	chdir(GAMEPATH);
	setenv("WINEPREFIX", GAMEPATH, 1);
	execl("/usr/bin/wine", "wine", GAMEPATH "/" GAME, (char*)NULL);
	perror("execl");
	exit(3);
}
