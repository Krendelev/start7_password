import urwid


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(char for char in password if not char.isalnum())


def has_not_only_symbols(password):
    has_alphanum = any(char.isalnum() for char in password)
    return has_alphanum and has_symbols(password)


def is_very_long(password):
    return len(password) > 12


def get_score(password):
    features = [
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
        has_not_only_symbols,
        is_very_long,
    ]
    return sum(2 if feature(password) else 0 for feature in features)


def on_ask_change(edit, new_edit_text):
    score = get_score(new_edit_text)
    reply.set_text(f"Passwords strength is {score} out of 14")


def on_exit_clicked(button):
    raise urwid.ExitMainLoop()


if __name__ == "__main__":
    ask = urwid.Edit("Enter your password: ", mask="*")
    reply = urwid.Text("")
    button = urwid.Button("Exit")
    div = urwid.Divider()
    pile = urwid.Pile([ask, div, reply, div, button])
    top = urwid.Filler(pile, valign="top")

    urwid.connect_signal(ask, "change", on_ask_change)
    urwid.connect_signal(button, "click", on_exit_clicked)

    urwid.MainLoop(top).run()
