# CCA_PY
CUI-based David Griffeath's Cycle Cellular Automaton made with Python

# Usage
1. Install terminal that can display truecolor ([TrueColour.md](https://gist.github.com/XVilka/8346728#now-supporting-truecolour) will be your help)
2. Install Python3.x
3. run `python main.py W H R T C N`
   W - field width (int)
   H - field height (int)
   R - neighborhood range (int)
   T - necessory count of next generation cells in the neighborhood (int)
   C - count of states (int)
   N - neighborhood type (N or M)

   example) `python main.py 20 10 1 3 5 N`
4. `Ctrl-C` to stop