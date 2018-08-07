# Directories
SRC_DIR = ./src
INC_DIR = ./src/inc
BUILD_DIR = ./bin

# Name of the app
APP_NAME = run

# Compiler
CC = g++

# Compiler Flags
CFLAGS = -O2 -std=c++11 -Wall -g -lpthread
LFLAGS = 
INCFLAGS = -I$(INC_DIR)

# Source and Object Files
SOURCES = $(wildcard $(SRC_DIR)/*.cpp)
OBJECTS = $(SOURCES:$(SRC_DIR)/%.cpp=$(BUILD_DIR)/%.o)


all: $(APP_NAME)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CFLAGS) $(INCFLAGS) -o $@ -c $<

$(APP_NAME): $(OBJECTS)
	$(CC) $(LFLAGS) -o $@ $^

clean:
	rm -rf $(BUILD_DIR)/*.o $(APP_NAME)
