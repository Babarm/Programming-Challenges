# Directories
SRC_DIR = ./src
BUILD_DIR = ./bin

# Name of the app
APP_NAME = run

# Compiler
CC = gcc

# Compiler Flags
CFLAGS = -Ofast -Wall
LFLAGS = -lm -lpthread
INCFLAGS = -I./src

# Source and Object Files
SOURCES = $(wildcard $(SRC_DIR)/*.c)
OBJECTS = $(SOURCES:$(SRC_DIR)/%.c=$(BUILD_DIR)/%.o)

all: $(APP_NAME)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) $(INCFLAGS) -o $@ -c $<

$(APP_NAME): $(OBJECTS)
	$(CC) -o $@ $^ $(LFLAGS)

clean:
	rm -rf $(BUILD_DIR)/*.o $(APP_NAME)
