/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const count = new Map();

  for (const ch of s) {
    count.set(ch, (count.get(ch) || 0) + 1);
  }

  for (const ch of t) {
    const nextCount = (count.get(ch) || 0) - 1;

    if (nextCount < 0) {
      return false;
    }

    if (nextCount === 0) {
      count.delete(ch);
    } else {
      count.set(ch, nextCount);
    }
  }

  return count.size === 0;
};