using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

var acceptedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".ToCharArray();
acceptedCharacters = acceptedCharacters.Concat(" !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~".ToCharArray()).ToArray();

ConsoleKey key;
int characterIndex = 0;
StringBuilder sb = new StringBuilder();
do
{
    key = Console.ReadKey(true).Key;
    if (key != ConsoleKey.Escape)
    {
        var index = Array.IndexOf(acceptedCharacters, key.ToString().ToCharArray()[0]);
        if (index == -1)
        {
            continue;
        }
        switch (key){
            case key.Key && characterIndex > 0 == ConsoleKey.Backspace:
                Console.Write("\b \b");
                characterIndex--;
                sb.Remove(sb.Length - 1, 1);
                break;
            case key.Key == ConsoleKey.Enter:
                Console.WriteLine();
                sb.AppendLine();
                break;
            default:
                Console.Write(acceptedCharacters[(index + characterIndex) % acceptedCharacters.Length]);
                characterIndex++;
                sb.Append(acceptedCharacters[(index + characterIndex) % acceptedCharacters.Length]);
                break;
        };
    }
} while (key != ConsoleKey.Escape);

Console.Clear();
Console.WriteLine(sb.ToString());

// Offer the choice to decode the string
if (Confirm("Do you want to decode the string? (y/n)"))
{
    Console.WriteLine("Enter the string to decode:");
    var input = Console.ReadLine();
    Console.WriteLine(Decode(input));
}

// Offer the choice to save the string
if (Confirm("Do you want to save the string? (y/n)"))
{
    Console.WriteLine("Enter the path to save the string:");
    var path = Console.ReadLine();
    try 
    {
        System.IO.File.WriteAllText(path, sb.ToString());
    }
    catch (Exception e)
    {
        Console.WriteLine("An error occured while saving the file: " + e.Message);
    }
}

static bool Confirm(string message)
{
    Console.WriteLine(message);
    ConsoleKey key;
    do
    {
        key = Console.ReadKey(true).Key;
        if (key == ConsoleKey.Y)
        {
            return true;
        }
        else if (key == ConsoleKey.N)
        {
            return false;
        }
    } while (key != ConsoleKey.Escape);
    return false;
}

// Create a funtion to decode the string
static string Decode(string input)
{
    var acceptedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".ToCharArray();
    acceptedCharacters = acceptedCharacters.Concat(" !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~".ToCharArray()).ToArray();
    var sb = new StringBuilder();
    foreach (var c in input)
    {
        var index = Array.IndexOf(acceptedCharacters, c);
        if (index == -1)
        {
            continue;
        }
        sb.Append(acceptedCharacters[(index - characterIndex) % acceptedCharacters.Length]);
    }
    return sb.ToString();
}