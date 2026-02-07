import { writable, type Writable } from "svelte/store";
type Workspace = 1 | 2 | 3 | 4;
export const workspaces: Workspace[] = [1, 2, 3, 4];
export const currentWorkspace = writable(workspaces[0]);
