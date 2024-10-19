# Western Astrology Program: Calculate user's zodiac sign based on birthdate and provide a summary

# Function to determine Western zodiac sign based on birthdate input
def determine_western_zodiac(day, month):
    # List of zodiac signs, date ranges, summaries, and links for further reading
    zodiac_signs = [
        ("Capricorn", (1, 1), (1, 19), 
         "Capricorns are known for their discipline, responsibility, and self-control. They excel at long-term planning and take their responsibilities seriously. They're natural leaders who value tradition and structure.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Aquarius", (1, 20), (2, 18), 
         "Aquarians are independent, original thinkers who love innovation and humanitarian causes. They are visionaries, often working to make the world a better place through progress and change.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Pisces", (2, 19), (3, 20), 
         "Pisces are compassionate, artistic, and deeply intuitive. Known for their sensitivity, they are empathetic and often connect deeply with others' emotions, making them caring and creative.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Aries", (3, 21), (4, 19), 
         "Aries are bold, ambitious, and passionate. As the first sign of the zodiac, they love to take initiative and are natural leaders. They are known for their energy, confidence, and desire to take on challenges.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Taurus", (4, 20), (5, 20), 
         "Taureans are known for their reliability, practicality, and patience. They value stability and are deeply connected to the material world, finding joy in life's simple pleasures.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Gemini", (5, 21), (6, 20), 
         "Geminis are curious, adaptable, and expressive. With a love for communication and learning, they are often social butterflies who excel at juggling multiple interests and ideas.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Cancer", (6, 21), (7, 22), 
         "Cancers are nurturing, empathetic, and protective. They value family and home above all else and are deeply in tune with their emotions, often caring for others with great compassion.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Leo", (7, 23), (8, 22), 
         "Leos are charismatic, confident, and natural leaders. Ruled by the Sun, they are warm-hearted and love to be the center of attention, using their creativity and charm to inspire others.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Virgo", (8, 23), (9, 22), 
         "Virgos are analytical, detail-oriented, and practical. They thrive on organization and helping others, often applying their critical thinking to solve problems and improve efficiency.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Libra", (9, 23), (10, 22), 
         "Libras are diplomatic, fair-minded, and lovers of harmony. They value balance in all aspects of life and are skilled at seeing different perspectives, making them great mediators.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Scorpio", (10, 23), (11, 21), 
         "Scorpios are intense, passionate, and resourceful. They are known for their determination and depth, often delving into life's mysteries with an unyielding focus and emotional intensity.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Sagittarius", (11, 22), (12, 21), 
         "Sagittarians are adventurous, optimistic, and freedom-loving. They have a strong desire to explore new horizons and seek knowledge, often drawn to travel and philosophical pursuits.", 
         "https://www.astrology.com/us/home.aspx"),
        ("Capricorn", (12, 22), (12, 31), 
         "Capricorns are known for their discipline, responsibility, and self-control. They excel at long-term planning and take their responsibilities seriously. They're natural leaders who value tradition and structure.", 
         "https://www.astrology.com/us/home.aspx")
    ]
    
    # Iterate through the list to find the user's zodiac sign
    for sign, start_date, end_date, summary, link in zodiac_signs:
        # Check if the month and day fall within the date range for each sign
        if (month == start_date[0] and day >= start_date[1]) or (month == end_date[0] and day <= end_date[1]):
            return sign, summary, link

    # If the date doesn't match any sign, return an error (this shouldn't happen)
    return None, "Invalid date", ""

# Main function to run the program
def main():
    # Prompt the user for their birthdate
    print("Welcome to the Western Astrology Program!")
    try:
        day = int(input("Enter your birth day (1-31): "))
        month = int(input("Enter your birth month (1-12): "))
        
        # Validate the input for day and month ranges
        if (month < 1 or month > 12) or (day < 1 or day > 31):
            print("Invalid date. Please enter a valid day and month.")
            return
        
        # Call the function to determine the zodiac sign, summary, and link
        zodiac_sign, summary, link = determine_western_zodiac(day, month)
        
        # Output the user's zodiac sign, summary, and link
        print(f"Your Western Zodiac sign is: {zodiac_sign}")
        print(f"Summary: {summary}")
        print(f"Learn more about your sign here: {link}")
    
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Please enter valid numerical values for day and month.")

# Run the program
if __name__ == "__main__":
    main()