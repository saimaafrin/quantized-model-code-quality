import java.util.*;
import java.text.SimpleDateFormat;
import java.text.ParseException;

class Problem {
    /**
     * Given a date in the format "MM dd yyyy", return the weekday of the date.
     * 
     * Example:
     * >>> convertDatesToWeekdays("11 15 1997")
     * "November 15, 1997 is a Saturday"
     * >>> convertDatesToWeekdays("01 01 2000")
     * "January 1, 2000 is a Saturday"
     * >>> convertDatesToWeekdays("07 04 1998")
     * "July 4, 1998 is a Saturday"
     */
    public static String convertDatesToWeekdays(String date)  {
        if (date == null || date.length() != 11) {
            throw new IllegalArgumentException("Invalid date string.");
        }
        String[] parts = date.split(" ");
        String month = parts[0];
        String day = parts[1];
        String year = parts[2];
        String fullDate = month + " " + day + ", " + year;
        SimpleDateFormat sdf = new SimpleDateFormat("MMM dd, yyyy");
        Date d;
        try {
            d = sdf.parse(fullDate);
        } catch (ParseException e) {
            return "Invalid date string.";
        }
        Calendar cal = Calendar.getInstance();
        cal.setTime(d);
        int weekday = cal.get(Calendar.DAY_OF_WEEK);
        String weekdayString = "";
        switch (weekday) {
            case Calendar.SUNDAY:
                weekdayString = "Sunday";
                break;
            case Calendar.MONDAY:
                weekdayString = "Monday";
                break;
            case Calendar.TUESDAY:
                weekdayString = "Tuesday";
                break;
            case Calendar.WEDNESDAY:
                weekdayString = "Wednesday";
                break;
            case Calendar.THURSDAY:
                weekdayString = "Thursday";
                break;
            case Calendar.FRIDAY:
                weekdayString = "Friday";
                break;
            case Calendar.SATURDAY:
                weekdayString = "Saturday";
                break;
        }
        return fullDate + " is a " + weekdayString;
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert convertDatesToWeekdays("02 05 2024").equals("February 5, 2024 is a Monday");
        assert convertDatesToWeekdays("01 12 2023").equals("January 12, 2023 is a Thursday");
        assert convertDatesToWeekdays("09 14 2013").equals("September 14, 2013 is a Saturday");
        System.out.println("All tests passed");
    }
}