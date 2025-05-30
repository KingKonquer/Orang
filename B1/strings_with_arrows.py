# filepath: c:\Users\Kingm\Orang\strings_with_arrows.py
def generate_arrows(text, pos_start, pos_end):
    result = ''
    # Highlight the error in the text using arrows
    lines = text.split('\n')
    for i in range(pos_start.ln, pos_end.ln + 1):
        line = lines[i]
        start = pos_start.col if i == pos_start.ln else 0
        end = pos_end.col if i == pos_end.ln else len(line)
        result += line + '\n'
        result += ' ' * start + '^' * (end - start) + '\n'
    return result
