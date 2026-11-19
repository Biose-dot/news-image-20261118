// news-image-20261118 entrypoint: hand the poster to the grader.
//
// The entry is a single image, entry.png beside this file (a 1024x1024 PNG
// summing up the world news of Wednesday 18 November 2026, drawn from
// source by build_image.py). The grader runs this program with no network
// and reads /output/entry.png, so the whole job here is a careful copy:
// make sure the output directory exists, copy the bytes unchanged, and
// confirm the copy is complete before exiting.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const sourcePath = fileURLToPath(new URL('./entry.png', import.meta.url));
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const targetPath = join(outputDir, 'entry.png');

mkdirSync(outputDir, { recursive: true });
copyFileSync(sourcePath, targetPath);

const sourceBytes = statSync(sourcePath).size;
const writtenBytes = statSync(targetPath).size;
if (writtenBytes !== sourceBytes) {
  throw new Error(
    `entry.png copy is incomplete: wrote ${writtenBytes} of ${sourceBytes} bytes`,
  );
}
console.log(`entry.png -> ${targetPath} (${writtenBytes} bytes)`);
