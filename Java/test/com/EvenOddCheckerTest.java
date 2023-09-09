package Experiments.Java.test.com;
import static org.junit.Assert.*;
import org.junit.Test;

import com.EvenOddChecker;



public class EvenOddCheckerTest {
    @Test
    public void testIsEvenWithEvenNumber() {
        assertTrue(EvenOddChecker.isEven(4));
    }

    @Test
    public void testIsEvenWithOddNumber() {
        assertFalse(EvenOddChecker.isEven(7));
    }
   
    @Test
    public void testIsEvenWithZero() {
        assertTrue(EvenOddChecker.isEven(0));
    }
   
}
