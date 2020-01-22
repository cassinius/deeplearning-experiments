import * as fs from 'fs';
import * as path from 'path';

const xkcd_file = path.join(__dirname, '../data/xkcd.json');
const sortColor = (a, b) => {
  // console.log(a.color.toString().localeCompare(b.color))
  return a.color.toString().localeCompare(b.color);
}

let xkcd = JSON.parse(fs.readFileSync(xkcd_file).toString());
xkcd.colors = xkcd.colors.sort(sortColor);

// console.log(xkcd);

interface V3 {
  x: number;
  y: number;
  z: number;
}
type ColorVec = {[key: string]: V3}
const vectors: ColorVec = {};

for ( let entry of xkcd.colors ) {
  vectors[entry.color] = hex2rgb(entry.hex);
}

console.log(vectors);
console.log(randomRgb());
console.log(findNearest(randomRgb()));



function hex2rgb(hex: string) : V3 {
  hex = hex.replace("#", "0x");
  const b = parseInt(hex) >> 16 & 255;
  const g = parseInt(hex) >> 8 & 255;
  const r = parseInt(hex) >> 0 & 255;
  return {x:r, y:g, z:b};
}


function randomRgb() : V3 {
  return {
    x: Math.floor(Math.random()*256),
    y: Math.floor(Math.random()*256),
    z: Math.floor(Math.random()*256)
  }
}


function findNearest(v: V3) {
  let keys = Object.keys(vectors);

  return keys.sort((a, b) => {
    const d1 = distance(vectors[a], v);
    const d2 = distance(vectors[b], v);
    return d1 - d2;
  });
}


function distance(a: V3, b: V3) : number {
  return Math.sqrt(
    (a.x - b.x) ** 2 +
    (a.y - b.y) ** 2 +
    (a.z - b.z) ** 2
  );
}