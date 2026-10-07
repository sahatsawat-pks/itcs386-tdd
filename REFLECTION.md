# Part B: Reflection

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?
* **Tests written:** 9 Tests function (12 assertions, 44 lines) inside `test_kitchen.py`
* **Lines of production code:** 54 lines from `kitchen.py`
* **Ratio (Test Lines : Production Lines):** 1:1.227
* **Observation:** The test suite nearly match the size of the production codebase. In TDD, this high ratio is typical because tests act as both living documentation and design specifications, covering setup, boundary cases, and expressions across small, focused assertions.

---

### 2. When was your bar red for the longest time, and what made it last so long?
The bar stayed red the longest during **Step A5/A6 (introducing `Sum` and transitioning to delegated reduction)**. 
* **What made it last:** Shifting from returning a `Quantity` inside itself class to returning a `Sum` broke the existing assumptions in `Converter.reduce`. We had to adjust the method signatures across multiple classes (`Quantity.reduce`, `Sum.reduce`, and `Converter.reduce`) before the test suite turned green again.
* **Lesson learned:** Whenever a step requires an architectural feature, keeping the step tiny, such as faking it with hardcoded values before wiring the full delegation—is crucial to keeping the red phase brief.

---

### 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
* **Fake It:** In Step A1, returning a constant `self.amount = 600` inside `Quantity.times(3)`, and in Step A6, having `Converter.reduce` just return `grams(500)`. This was the right choice because it proved that the test runner, import paths, and assertions were wired up correctly before writing real logic.
* **Triangulation:** In Steps A1 and A2, writing `test_multiplication` with factor 3 and `test_multiplication_by_two` with factor 2. This forced out the constant `600` and drove the generalized formula `self.amount * multiplier`. It was the right choice because it established the general multiplication rule without guessing edge cases early.
* **Obvious Implementation:** In Step A7, implementing `Converter.rate(from_unit, to_unit)` with `if from_unit == to_unit: return 1; return self.rates[(from_unit, to_unit)]`. This was the right choice because a dictionary lookup with an identity short-circuit is standard, straightforward Python and did not benefit from being broken down into fake constant returns.

---

### 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
* **Still on the test list:**
  * `Sum.plus(other)`: Chained additions like `(grams(100).plus(ounces(1))).plus(grams(50))` currently fail because `Sum` does not implement `plus`. Implementing this is essential to make `Sum` fully interchangeable with `Quantity` as an `Expression`.
  * Missing conversion rate handling: Defining the expected behavior (e.g., raising a clear `KeyError` or custom exception) when a rate from unit A to B does not exist in `Converter.rates`.
* **Speculation to delete:**
  * Automatic rate inversion (deriving `g -> oz` as `1 / rate` when `oz -> g` is added): This introduces rounding and precision issues and should be omitted until explicitly demanded by a recipe requirement.* `Sum.plus(other)`: Chained additions like `(grams(100).plus(ounces(1))).plus(grams(50))` currently fail because `Sum` does not implement `plus`. Implementing this is essential to make `Sum` fully interchangeable with `Quantity` as an `Expression`.
  * Missing conversion rate handling: Defining the expected behavior (e.g., raising a clear `KeyError` or custom exception) when a rate from unit A to B does not exist in `Converter.rates`.
  * Adding subtraction (`minus`) or division: Speculative math operations that are unnecessary until a concrete user story requires them.
* **Speculation to delete:**
  * Automatic rate inversion (deriving `g -> oz` as `1 / rate` when `oz -> g` is added): This introduces rounding and precision issues and should be omitted until explicitly demanded by a recipe requirement.
  * Adding subtraction (`minus`) or division: Speculative math operations that are unnecessary until a concrete user story requires them.

---

### 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
No. An up-front, paper-based design would almost certainly have viewed `Quantity` as a passive data holder (DTO) and placed all conversion logic inside `Converter.reduce` using procedural `isinstance(source, Sum)` or unit-matching `if/elif` blocks. The method `Quantity.reduce(converter, unit)` emerged solely because `Converter.reduce(source, unit)` required a uniform, polymorphic interface to reduce both leaf nodes (`Quantity`) and composite nodes (`Sum`) without inspecting their concrete types.

---

### 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
Writing tests after the code in Part 0 (`leap.py`, `bank.py`, `shipping.py`) felt like quality assurance and compliance checking—verifying boundary conditions and exceptions against fixed logic. In contrast, writing tests first in Part A felt like architecture design. Writing `assert flour.times(3) == grams(600)` forced `Quantity` to become an immutable Value Object, and writing `test_mixed_addition` alongside `test_sum_times` completely shaped the architecture into the Composite/Interpreter pattern. The tests acted as the first consumer of the API, highlighting design friction immediately.