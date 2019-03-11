
import numpy as np
import pdb

class Graph:
    def __init__(self, image):
        self.from_image(image)

    def sousedi(self, a):
        return self.seznamySousedu[a]

    def BFS(self, x):
        # Vzdalenost do bodu x z bodu x je 0
        self.vzdalenost[x] = 0
        # inicializujeme seznam ukolu startovnim vrcholem x
        self.ukoly.append(x)
        
        # dokud mame ukoly, budeme je postupne vyrizovat
        while(len(self.ukoly)>0):
            # vyjmeme ze seznamu ukolu nejstarsi ukol
            # a ulozime ho do promenne ukol. Je to cislo vrcholu,
            # ktery mame prohledat.
            ukol = self.ukoly.pop(0)
            () # vizualizace a pozastaveni vypoctu

            # Naplanujeme prohledani vsech sousedu ukolu, ktere
            # jeste nebyly navstiveny a prohledame jejich sousedy.
            # U kazdeho souseda vyplnime jeho vzdalenost a tim jej
            # oznacime za prozkoumaneho.
            for s in self.sousedi(ukol):
                if(self.vzdalenost[s] < 0):
                    self.vzdalenost[s] = self.vzdalenost[ukol]+1
                    self.ukoly.append(s)
        n_dosazenych = np.sum(self.vzdalenost != -1)
        n_zdi = np.sum(self.zdi != 0)
        return (self.N - n_dosazenych - n_zdi)
        
    def from_image(self, image):
        h, w  = image.shape
        self.N = w*h               # N je pocet pixelu v obrazku
        self.zdi = np.zeros(self.N)          # zdi[i] je 1, pokud na policku i je zed.
        self.vzdalenost = -np.ones(self.N) # vzdalenost[i] je nejkratsi vzdalenost 
                              # od startu do i, nebo -1, pokud je neznama.
        self.ukoly = []            # seznam ukolu pro BFS.
        for i in range(h):     # i je cislo radku.vypisStav
            for j in range(w): # j je cislo sloupce.
                if image[i,j] != 0:
                    self.zdi[w*i+j] = 1
        self.seznamySousedu = []
        for v in range(self.N):
            i = v / w # i je cislo radku
            j = v % w # j je cislo sloupce. Operace modulo (%) znamena zbytek po deleni
            self.seznamySousedu.append([])
            if (v+w < self.N and self.zdi[v+w] == 0):
                self.seznamySousedu[v].append(v+w)
            if (v-w >= 0 and self.zdi[v-w] == 0):
                self.seznamySousedu[v].append(v-w)
            if ((v%w)+1 < w and self.zdi[v+1] == 0):
                self.seznamySousedu[v].append(v+1)
            if ((v%w)-1 >= 0 and self.zdi[v-1] == 0):
               self.seznamySousedu[v].append(v-1)
