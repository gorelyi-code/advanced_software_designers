import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        InputHandler inputHandler = new InputHandler();
        CircularShifter circularShifter = new CircularShifter(inputHandler);
        Alphabetizer alphabetizer = new Alphabetizer(circularShifter);
        OutputHandler outputHandler = new OutputHandler(alphabetizer);

        List<String> lines = List.of("the quick brown fox", "jumps over the lazy dog");
        inputHandler.processInput(lines);
    }
}

interface Subscriber<T> {
    void handle(T data);
}

class InputHandler {
    private final List<Subscriber<String>> subscribers = new ArrayList<>();

    public void subscribe(Subscriber<String> subscriber) {
        subscribers.add(subscriber);
    }

    public void processInput(List<String> lines) {
        for (String line : lines) {
            for (Subscriber<String> subscriber : subscribers) {
                subscriber.handle(line);
            }
        }
    }
}

class CircularShifter implements Subscriber<String> {
    private final List<Subscriber<List<String>>> subscribers = new ArrayList<>();

    public CircularShifter(InputHandler inputHandler) {
        inputHandler.subscribe(this);
    }

    public void subscribe(Subscriber<List<String>> subscriber) {
        subscribers.add(subscriber);
    }

    @Override
    public void handle(String line) {
        String[] words = line.split(" ");
        List<String> shifts = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            String shifted = String.join(" ", rotate(words, i));
            shifts.add(shifted);
        }
        for (Subscriber<List<String>> subscriber : subscribers) {
            subscriber.handle(shifts);
        }
    }

    private String[] rotate(String[] words, int index) {
        String[] result = new String[words.length];
        System.arraycopy(words, index, result, 0, words.length - index);
        System.arraycopy(words, 0, result, words.length - index, index);
        return result;
    }
}

class Alphabetizer implements Subscriber<List<String>> {
    private final List<Subscriber<List<String>>> subscribers = new ArrayList<>();

    public Alphabetizer(CircularShifter circularShifter) {
        circularShifter.subscribe(this);
    }

    public void subscribe(Subscriber<List<String>> subscriber) {
        subscribers.add(subscriber);
    }

    @Override
    public void handle(List<String> shifts) {
        Collections.sort(shifts);
        for (Subscriber<List<String>> subscriber : subscribers) {
            subscriber.handle(shifts);
        }
    }
}

class OutputHandler implements Subscriber<List<String>> {
    public OutputHandler(Alphabetizer alphabetizer) {
        alphabetizer.subscribe(this);
    }

    @Override
    public void handle(List<String> sortedList) {
        for (String line : sortedList) {
            System.out.println(line);
        }
    }
}
