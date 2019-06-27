import time


class SlideUp:
    def __init__(self):
        self.original_pos = []

    def get_pos(self, window, canvas, tag):
        z = canvas.find_withtag(tag)
        pos = canvas.coords(z)
        if len(self.original_pos) == 0:
            self.original_pos = pos
        print(self.original_pos)
        x = self.original_pos[0]
        y = self.original_pos[1]
        self.move_text(x, y, z, pos, window, canvas, tag)

    def move_text(self, x, y, z, pos, window, canvas, tag):
        if self.original_pos[1] < 65:
            print("Unable to execute. Value 'y' must be greater than 65.")
            return
        if pos > [x, y-25]:
            canvas.coords(z, pos[0], pos[1] - 1)
            time.sleep(0.01)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos > [x, y-45]:
            canvas.coords(z, pos[0], pos[1] - 1)
            time.sleep(0.015)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos > [x, y-55]:
            canvas.coords(z, pos[0], pos[1] - 1)
            time.sleep(0.03)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos > [x, y-60]:
            canvas.coords(z, pos[0], pos[1] - 1)
            time.sleep(0.04)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos > [x, y-65]:
            canvas.coords(z, pos[0], pos[1] - 1)
            time.sleep(0.1)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos > [x, y-66]:
            return


class Slide2Up:
    def __init__(self):
        self.original_pos = []

    def get_pos(self, window, canvas, tag):
        z = canvas.find_withtag(tag)
        z1 = z[0]
        z2 = z[1]
        pos1 = canvas.coords(z1)
        pos2 = canvas.coords(z2)
        if len(self.original_pos) == 0:
            self.original_pos.append(pos1[0])
            self.original_pos.append(pos1[1])
            self.original_pos.append(pos2[0])
            self.original_pos.append(pos2[1])
        x1 = self.original_pos[0]
        y1 = self.original_pos[1]
        x2 = self.original_pos[2]
        y2 = self.original_pos[3]
        self.move_text(x1, y1, x2, y2, z1, z2, pos1, pos2, window, canvas, tag)

    def move_text(self, x1, y1, x2, y2, z1, z2, pos1, pos2, window, canvas, tag):
        if self.original_pos[1] < 65 and self.original_pos[3] < 65:
            print("Unable to execute. Value 'y' must be greater than 65.")
            return
        if pos1 > [x1, y1-25] and pos2 > [x2, y2-25]:
            canvas.coords(z1, pos1[0], pos1[1] - 1)
            canvas.coords(z2, pos2[0], pos2[1] - 1)
            time.sleep(0.01)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos1 > [x1, y1-45] and pos2 > [x2, y2-45]:
            canvas.coords(z1, pos1[0], pos1[1] - 1)
            canvas.coords(z2, pos2[0], pos2[1] - 1)
            time.sleep(0.015)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos1 > [x1, y1-55] and pos2 > [x2, y2-55]:
            canvas.coords(z1, pos1[0], pos1[1] - 1)
            canvas.coords(z2, pos2[0], pos2[1] - 1)
            time.sleep(0.03)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos1 > [x1, y1-60] and pos2 > [x2, y2-60]:
            canvas.coords(z1, pos1[0], pos1[1] - 1)
            canvas.coords(z2, pos2[0], pos2[1] - 1)
            time.sleep(0.04)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos1 > [x1, y1 - 65] and pos2 > [x2, y2 - 65]:
            canvas.coords(z1, pos1[0], pos1[1] - 1)
            canvas.coords(z2, pos2[0], pos2[1] - 1)
            time.sleep(0.1)
            window.update_idletasks()
            self.get_pos(window, canvas, tag)
        elif pos1 > [x1, y1-66] and pos1 > [x1, y1-66]:
            return

