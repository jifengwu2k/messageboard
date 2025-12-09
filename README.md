# `messageboard`

A synchronization primitive containing a value, allowing threads to concurrently set the value and peek the most recently set value.

## Features

- Thread-safe.
- `.set(value)` sets the value.
- `.peek()` peeks the most recently set value. If no value is set yet, `.peek()` blocks until a value is set.

## Usage

```python
from __future__ import print_function
import random

random.seed(42)
import threading
import time

from messageboard import MessageBoard


def writer(message_board):
    for i in range(10):
        message_board.set(i)
        print('Written', i)
        time.sleep(1)


def reader(sticky_value):
    for i in range(10):
        if random.random() > 0.5:
            sticky_value.peek()
            print('Peeked', i)
        time.sleep(1)


board = MessageBoard()

writer_thread = threading.Thread(target=writer, args=(board,))
writer_thread.daemon = True

reader_thread = threading.Thread(target=reader, args=(board,))
reader_thread.daemon = True

writer_thread.start()
reader_thread.start()

writer_thread.join()
reader_thread.join()
```

This produces the following output:

```
Written 0
Peeked 0
Written 1
Written 2
Written 3
Written 4
Peeked 4
Written 5
Peeked 5
Written 6
Peeked 6
Written 7
Written 8
Written 9
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).