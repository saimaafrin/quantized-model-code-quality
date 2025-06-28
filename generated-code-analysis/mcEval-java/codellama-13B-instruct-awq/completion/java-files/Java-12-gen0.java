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
        // Initialize variables
        String[] dateList = date.split(" ");
        String month = dateList[0];
        int month_int = Integer.parseInt(month);
        String day = dateList[1];
        String year = dateList[2];
        int day_int = Integer.parseInt(day);
        int year_int = Integer.parseInt(year);
        String weekday = "";

        // Parse date into a Date object
        SimpleDateFormat sdf = new SimpleDateFormat("MM dd yyyy");
        Date date_object = new Date(0);
        try {
            date_object = sdf.parse(date);
        }
        catch (ParseException ex) {
            System.out.println(ex);
        }

        // Convert Date object into a Calendar object
        Calendar cal = Calendar.getInstance();
        cal.setTime(date_object);
        int weekday_int = cal.get(Calendar.DAY_OF_WEEK);

        // Determine the weekday
        switch (weekday_int) {
            case 1:
                weekday = "Sunday";
                break;
            case 2:
                weekday = "Monday";
                break;
            case 3:
                weekday = "Tuesday";
                break;
            case 4:
                weekday = "Wednesday";
                break;
            case 5:
                weekday = "Thursday";
                break;
            case 6:
                weekday = "Friday";
                break;
            case 7:
                weekday = "Saturday";
                break;
            default:
                weekday = "Error: Please enter a valid date.";
        }

        // Return the weekday
        return month + " " + day + ", " + year + " is a " + weekday;
    }
    public static void main(String[] args) {
        // Test the function with different test cases
        assert convertDatesToWeekdays("02 05 2024").equals("February 5, 2024 is a Monday");
        assert convertDatesToWeekdays("01 12 2023").equals("January 12, 2023 is a Thursday");
        assert convertDatesToWeekdays("09 14 2013").equals("September 14, 2013 is a Saturday");
        System.out.println("All tests passed");
    }
}