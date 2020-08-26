package com.company;
import java.io.IOException;
class Main{
    public static void main(String[] args) throws IOException {
    System.out.println("Downloading vk_api...");
    Process process = Runtime.getRuntime().exec("cmd /c pip install vk_api");
    System.out.println("Done, you can close the window.");
    System.console().readLine();
    }
}
