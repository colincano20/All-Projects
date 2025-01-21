#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Game {
public:
    string name;
    int price;
    int inventory; // Number of copies available

    Game(string gameName, int gamePrice, int gameInventory)
        : name(gameName), price(gamePrice), inventory(gameInventory) {}

    void displayGame() const {
        cout << "Game: " << name << ", Price: $" << price << ", Copies: " << inventory << endl;
    }
};

class GameStore {
public:
    vector<Game> games;

    void addGame(string name, int price, int inventory) {
        // Check if the game already exists in the store
        for (auto& game : games) {
            if (game.name == name) {
                game.inventory += inventory; // Increase the inventory
                cout << "Added " << inventory << " more copies of " << name << " to the store." << endl;
                return;
            }
        }
        // If the game doesn't exist, add it as a new game
        games.push_back(Game(name, price, inventory));
        cout << "Game added: " << name << " with " << inventory << " copies." << endl;
    }

    void buyGame(string name) {
        for (auto& game : games) {
            if (game.name == name) {
                if (game.inventory > 0) {
                    game.inventory--; // Reduce inventory
                    cout << "You bought: " << name << " for $" << game.price << endl;
                    if (game.inventory == 0) {
                        
                        cout << "No more copies of " << name << " are available!" << endl;
                    }
                    return;
                } else {
                    cout << "Sorry, " << name << " is out of stock!" << endl;
                    return;
                }
            }
        }
        cout << "Game not found in the store!" << endl;
    }

    void displayStoreGames() const {
        if (games.empty()) {
            cout << "No games in the store yet!" << endl;
        } else {
            cout << "Games in the store:" << endl;
            for (const auto& game : games) {
                game.displayGame();
            }
        }
    }
};

int main() {
    GameStore store;
    int choice;

    do {
        cout << "\nMenu:\n1. Add Game to Store\n2. Buy Game\n3. View Store Games\n4. Exit\nEnter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                string name;
                int price, inventory;
                cout << "Enter the name of the game: ";
                cin.ignore(); // Clear the input buffer
                getline(cin, name);
                cout << "Enter the price of the game: ";
                cin >> price;
                cout << "Enter the number of copies: ";
                cin >> inventory;
                store.addGame(name, price, inventory);
                break;
            }
            case 2: {
                string name;
                cout << "Enter the name of the game to buy: ";
                cin.ignore(); // Clear the input buffer
                getline(cin, name);
                store.buyGame(name);
                break;
            }
            case 3:
                store.displayStoreGames();
                break;
            case 4:
                cout << "Exiting the program. Goodbye!" << endl;
                break;
            default:
                cout << "Invalid choice! Try again." << endl;
        }
    } while (choice != 4);

    return 0;
}
