import * as fs from 'fs';
import * as path from 'path';

const xkcd_file = path.join(__dirname, '../data/xkcd.json');

const xkcd = JSON.parse(fs.readFileSync(xkcd_file).toString());

// console.log(xkcd);

interface V3 {
  r: number;
  g: number;
  b: number;
}
type ColorVec = {[key: string]: V3}
const vectors: ColorVec = {};

for ( let entry of xkcd.colors ) {
  vectors[entry.color] = hex2rgb(entry.hex);
}

console.log(vectors);



function hex2rgb(hex: string) : V3 {
  hex = hex.replace("#", "0x");
  const b = parseInt(hex) >> 16 & 255;
  const g = parseInt(hex) >> 8 & 255;
  const r = parseInt(hex) >> 0 & 255;
  return {r, g, b};
}