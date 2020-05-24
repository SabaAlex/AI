from ui.ACOUI import ACOUI

if __name__ == '__main__':
    #Internally the fitness scale is from 1 to n * n + 2 * n + 1, 1 being the best solution, the printing is done with a scale from 0 to n * n + 2 * n
    ui = ACOUI()
    ui.runUI()
