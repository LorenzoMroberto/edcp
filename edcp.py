import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import os
import sys
class SimpleEditor(ctk.CTk):
    def __init__(self, initial_file=None):
        super().__init__()
        
        # Configure window
        self.title("edcp ")
        self.geometry("800x600")
        
        # Set theme to system
        ctk.set_appearance_mode("dark")  # Default to dark theme
        ctk.set_default_color_theme("blue")  # Use blue theme as default
        
        # Create line numbers frame
        self.line_numbers_frame = ctk.CTkFrame(self, width=50)
        self.line_numbers_frame.grid(row=0, column=0, sticky="ns")
        
        # Create line numbers text widget
        self.line_numbers = tk.Text(
            self.line_numbers_frame,
            width=4,
            padx=5,
            pady=5,
            state='disabled',
            wrap='none',
            font=("Consolas", 12),
            bg="#252525",  # Slightly darker than main editor
            fg="#858585",  # Gray text
            bd=0,
            highlightthickness=0
        )
        self.line_numbers.pack(side='left', fill='y', expand=True)
        
        # Create text area with scrollbar
        self.text_area = tk.Text(
            self,
            wrap="none",  # Disable word wrapping
            undo=True,
            font=("Consolas", 12),
            bg="#2b2b2b",  # Dark background
            fg="#ffffff",  # White text
            insertbackground="#ffffff",  # White cursor
            selectbackground="#404040",  # Dark selection background
            selectforeground="#ffffff",  # White selection text
            tabs=(60),  # Custom tab size (in pixels)
            insertwidth=2  # Make cursor slightly wider
        )
        
        # Create scrollbars
        self.v_scrollbar = ctk.CTkScrollbar(
            self,
            orientation="vertical",
            command=self._scroll_both
        )
        self.h_scrollbar = ctk.CTkScrollbar(
            self,
            orientation="horizontal",
            command=self.text_area.xview
        )
        
        # Configure text area with scrollbars
        self.text_area.configure(
            yscrollcommand=self._update_scroll_and_line_numbers,
            xscrollcommand=self.h_scrollbar.set
        )
        
        # Grid layout
        self.text_area.grid(row=0, column=1, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=2, sticky="ns")
        self.h_scrollbar.grid(row=1, column=1, sticky="ew")
        
        # Configure grid weights
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Bind Ctrl+S to save
        self.bind("<Control-s>", self.save_file)
        
        # Bind events for line numbers update
        self.text_area.bind("<KeyRelease>", self._update_line_numbers)
        self.text_area.bind("<MouseWheel>", self._update_line_numbers)
        self.text_area.bind("<Button-4>", self._update_line_numbers)  # Linux scroll up
        self.text_area.bind("<Button-5>", self._update_line_numbers)  # Linux scroll down
        
        # File path variable
        self.current_file = None
        
        # Open file if provided as argument, otherwise show file dialog
        if initial_file and os.path.exists(initial_file):
            self.load_file(initial_file)
        else:
            self.open_file()
    
    def _scroll_both(self, *args):
        """Scroll both text and line numbers together"""
        self.text_area.yview(*args)
        self._update_line_numbers()
    
    def _update_scroll_and_line_numbers(self, *args):
        """Update scrollbar and line numbers"""
        self.v_scrollbar.set(*args)
        self._update_line_numbers()
    
    def _update_line_numbers(self, event=None):
        """Update the line numbers display"""
        # Get current view of text widget
        first_visible_line = int(self.text_area.index("@0,0").split('.')[0])
        last_visible_line = int(self.text_area.index("@0,%d" % self.text_area.winfo_height()).split('.')[0])
        
        # Get total lines
        total_lines = int(self.text_area.index('end-1c').split('.')[0])
        
        # Generate line numbers for visible area plus some padding
        line_numbers_text = "\n".join(str(i) for i in range(first_visible_line, min(last_visible_line + 5, total_lines + 1)))
        
        # Update line numbers widget
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')
        self.line_numbers.insert('1.0', line_numbers_text)
        self.line_numbers.config(state='disabled')
        
        # Adjust line numbers colors for current line
        current_line = int(self.text_area.index(tk.INSERT).split('.')[0])
        self.line_numbers.tag_remove('current_line', '1.0', 'end')
        self.line_numbers.tag_add('current_line', f'{current_line}.0', f'{current_line}.end')
        self.line_numbers.tag_config('current_line', foreground='#ffffff')  # White for current line
    
    def load_file(self, file_path):
        self.current_file = file_path
        self.title(f"edcp => ( {os.path.basename(file_path)} )")
        
        # Clear text area
        self.text_area.delete(1.0, tk.END)
        
        # Read file in chunks
        chunk_size = 1024 * 1024  # 1MB chunks
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                self.text_area.insert(tk.END, chunk)
                self.update_idletasks()  # Update UI while loading
        
        # Update line numbers after loading
        self._update_line_numbers()
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.load_file(file_path)
    
    def save_file(self, event=None):
        if self.current_file:
            # Get all text content
            content = self.text_area.get(1.0, tk.END)
            
            # Write content to file
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(content)

if __name__ == "__main__":
    # Get file path from command line arguments if provided
    initial_file = sys.argv[1] if len(sys.argv) > 1 else None
    
    app = SimpleEditor(initial_file)
    app.mainloop()
