from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
api_key="AIzaSyC155ew2ZwsY-LTzMmMZdV1t4i8ZKomtUE",
base_url="https://generativelanguage.googleapis.com/v1beta/")

#chain of thought 


SYSTEM_PROMPT = """

you are an expert in the coding domain and only answer to the questions realted to the coding. your name is coder_AI 
You work on the START,PLAN and OUTPUT steps.
you need to first plan what needs to be done.the plan can be multiple steps 
once you think enought plan has been done finally you can give me the output


Rule:
-Strictly follow the give json output format 
-only run one steps at a time 
- the sequence of the steps is START (where user gives an input),PLAN (that can be multiple times ) and finally OUTPUT (which sis goint to be the output to the user)

Output Format:
{
"Step" : "START" or "PLAN" or "OUTPUT",
"CONTENT" : "string"
}

Examples:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN": "content": "Seems like user is interested in math
problem" }
PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve
this using BODMAS method" }
PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be
done here" }
PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is
15" }
PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10"}
PLAN: { "step": "PLAN": "content": "We must perform divide that 15/10 = 1.5"}
PLAN: { "step": "PLAN": "content": "We must perform add now that 2+1.5 = 3.5"}
PLAN: { "step": "OUTPUR": "content": "the final ans is 3.5"}






"""


response = client.chat.completions.create(
model="gemini-2.5-flash",
response_format={"type":"json_object"},
messages=[
    { "role": "system", "content":SYSTEM_PROMPT},
    { "role": "user", "content": "write a code in java for palindrome" },
    {"role": "assistant" , "content" : json.dumps({
"Step": "START",
"CONTENT": "The user wants Java code to check if a string is a palindrome."
})},
   {"role": "assistant" , "content" : json.dumps({
"Step": "PLAN",
"CONTENT": "The user wants Java code for checking if a string is a palindrome. I will create a Java class with a method to check for palindromes and a main method to demonstrate its usage."
})}
,
  {"role": "assistant" , "content" : json.dumps({
"Step": "PLAN",
"CONTENT": "First, I'll define a method `isPalindrome` that takes a string as input. Inside this method, I will convert the string to lowercase to handle case-insensitivity. Then, I'll use two pointers, one starting from the beginning and one from the end, to compare characters. If at any point the characters don't match, it's not a palindrome. If the loop completes, it is a palindrome. Finally, I will provide a `main` method to test with example strings."
})}




    ]

)

print(response.choices [0].message.content)
# FINAL OUTPUT
# {
# "Step": "OUTPUT",
# "CONTENT": "```java\npublic class PalindromeChecker {\n\n    /**\n     * Checks if a given string is a palindrome.\n     * A string is a palindrome if it reads the same forwards and backwards.\n     * This method ignores case and non-alphanumeric characters for comparison.\n     *\n     * @param text The string to check.\n     * @return true if the string is a palindrome, false otherwise.\n     */\n    public static boolean isPalindrome(String text) {\n        // Handle null or empty string case\n        if (text == null || text.isEmpty()) {\n            return true; // Or false, depending on definition. For simplicity, we consider empty/null palindromic.\n        }\n\n        // Convert to lowercase and remove non-alphanumeric characters\n        // This makes the comparison case-insensitive and ignores punctuation/spaces.\n        String cleanedText = text.toLowerCase().replaceAll(\"[^a-z0-9]\", \"\");\n\n        int left = 0;\n        int right = cleanedText.length() - 1;\n\n        while (left < right) {\n            if (cleanedText.charAt(left) != cleanedText.charAt(right)) {\n                return false; // Characters do not match\n           
#  }\n            left++;\n            right--;\n        }\n        return true; // All characters matched\n    }\n\n    public static void main(String[] args) {\n        // Test cases\n        String[] testStrings = {\n            \"madam\",\n            \"racecar\",\n            \"A man, a plan, a canal: Panama\",\n            \"hello\",\n            \"Java\",\n            \"\", // Empty string\n            null, // Null string\n            \"Was it a car or a cat I saw?\"\n        };\n\n        for (String s : testStrings) {\n            System.out.println(\"\\\"\" + s + \"\\\" is a palindrome: \" + isPalindrome(s));\n        }\n\n        System.out.println(\"\\n--- Alternative implementation (case-sensitive, considers all chars) ---\");\n        // Alternative for strictly case-sensitive and all character comparison\n        String str1 = \"madam\";\n        String str2 = \"Madam\";\n        String str3 = \"race car\";\n        System.out.println(\"\\\"\" + str1 + \"\\\" is a strict palindrome: \" + isStrictPalindrome(str1));\n        System.out.println(\"\\\"\" + str2 + \"\\\" is a strict palindrome: \" + isStrictPalindrome(str2));\n        System.out.println(\"\\\"\" + str3 + \"\\\" is a strict palindrome: \" + isStrictPalindrome(str3));\n\n    }\n\n    /**\n     * Alternative strict palindrome check: case-sensitive and considers all characters.\n     * @param text The string to check.\n     * @return true if the string is a strict palindrome, false otherwise.\n     */\n    public static boolean isStrictPalindrome(String text) {\n        if (text == null || text.isEmpty()) {\n            return true;\n        }\n        int left = 0;\n        int right = text.length() - 1;\n\n        while (left < right) {\n           
#  if (text.charAt(left) != text.charAt(right)) {\n                return false;\n            }\n            left++;\n            right--;\n        }\n        return true;\n    }\n}\n```"
# }