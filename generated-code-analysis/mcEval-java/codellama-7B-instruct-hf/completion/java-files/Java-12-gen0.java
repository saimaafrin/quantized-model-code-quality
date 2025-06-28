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
        SimpleDateFormat sdf = new SimpleDateFormat("MM dd yyyy");
        Date convertedDate = new Date();
        String day = "";
        String month = "";
        String year = "";
        String weekday = "";
        try {
            convertedDate = sdf.parse(date);
            Calendar c = Calendar.getInstance();
            c.setTime(convertedDate);
            day = "" + c.get(Calendar.DAY_OF_MONTH);
            month = "" + c.get(Calendar.MONTH);
            year = "" + c.get(Calendar.YEAR);
            weekday = c.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, Locale.ENGLISH);
        } catch (ParseException e) {
            return "The date " + date + " is invalid. Please make sure that it is in the format MM dd yyyy";
        }

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