"""Create a file"""
def create_file(data, sort_choice):
    """Function to create a file"""
    file_name = str(f'order_by_{sort_choice}.txt')
    try:
        with open(file_name, 'w') as final_text:
            final_text_str =''
            for element in data:
                sequence = element['sequence']
                size = element['size']
                priority = element['priority']
                if priority == 2:
                    priority = 'HIGH'
                elif priority == 1:
                    priority = 'MEDIUM'
                elif priority == 0:
                    priority = 'LOW'
                final_text_str = str(f'{final_text_str}')+str(f'{sequence} {size} {priority}\n')
            final_text.write(final_text_str)
    except FileNotFoundError:
        pass
    