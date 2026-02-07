// place files you want to import through the `$lib` alias in this folder.
//
export const sleep = async (t: number) => new Promise<number>((resolve) => setTimeout(() => resolve(t), t));
