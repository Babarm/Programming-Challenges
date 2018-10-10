APP_NAME = run

CC = gcc

CFLAGS = -Ofast -Wall
LFLAGS = -lm
INCFLAGS = -I./src

SOURCE_FILES = $(wildcard ./src/*.c)
OBJECT_FILES = $(SOURCE_FILES:./src/%.c=./bin/%.o)

all: $(APP_NAME)

$(APP_NAME): $(OBJECT_FILES)
	$(CC) $(LFLAGS) -o $@ $^

./bin/%.o: ./src/%.c
	$(CC) $(CFLAGS) $(INCFLAGS) -o $@ -c $<

clean:
	rm -rf ./bin/*.o $(APP_NAME)
