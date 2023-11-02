package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine, Drink {

  private static VendingMachine instance;
  private int quarter;
  private String name;
  private boolean isFizzy;

  private VendingMachineImpl() {
    this.quarter = 0;
    this.name = "";
    this.isFizzy = true;
  }

  public static VendingMachine getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }

    return instance;
  }

  @Override
  public void insertQuarter() {
    quarter++;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    this.name = name;

    if (name.equals("ScottCola") && quarter < 4) {
      throw new NotEnoughMoneyException();
    } else if (name.equals("ScottCola") && quarter >= 4) {
      this.isFizzy = !isFizzy;
      return this;
    } else if (name.equals("KarenTea") && quarter < 4) {
      throw new NotEnoughMoneyException();
    } else if (name.equals("KarenTea") && quarter >= 4) {
      this.isFizzy = !isFizzy;
      return this;
    } else {
      throw new UnknownDrinkException();
    }
  }

  @Override
  public String getName() {
    return name;
  }

  @Override
  public boolean isFizzy() {
    return isFizzy;
  }
}
