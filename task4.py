import numpy as np
import unittest

def genrandate(mean, variance, num_samples):
    low = max(mean - variance, 0)
    high = min(mean + variance + 1, 90)
    if low >= high: 
        return np.full(num_samples, low) 
    return np.random.randint(low, high, num_samples)

def calcuaver(threat_scores):
    return np.mean(threat_scores)

def calcuaggred(department_scores, importance_tags):
    weighted_sum = sum(score * importance for score, importance in zip(department_scores, importance_tags))
    total_importance = sum(importance_tags)
    aggregated_score = weighted_sum / total_importance
    return min(max(aggregated_score, 0), 90)

class testcybersec(unittest.TestCase):

    def test_calcuaver(self):
        scores = [20, 30, 40, 50]
        self.assertAlmostEqual(calcuaver(scores), 35, places=2)
    
    def test_calcuaggred(self):
        department_scores = [30, 40, 50]
        importance_tags = [1, 2, 3]
        expected_weighted_average = (30*1 + 40*2 + 50*3) / (1 + 2 + 3)
        self.assertAlmostEqual(calcuaggred(department_scores, importance_tags), expected_weighted_average, places=2)

    def testbalance(self):
        department_scores = [genrandate(30, 10, 50).mean() for _ in range(5)]
        importance_tags = [3, 3, 3, 3, 3]
        agg_score = calcuaggred(department_scores, importance_tags)
        self.assertTrue(0 <= agg_score <= 90)

    def testcasehigh(self):
        department_scores = [genrandate(30, 10, 50).mean() for _ in range(4)]
        high_threat_dept = genrandate(80, 5, 100).mean()
        department_scores.append(high_threat_dept)
        importance_tags = [1, 1, 1, 1, 5]
        agg_score = calcuaggred(department_scores, importance_tags)
        self.assertTrue(0 <= agg_score <= 90)

    def testcaselow(self):
        department_scores = [genrandate(30, 10, 50).mean() for _ in range(4)]
        high_threat_dept = genrandate(80, 5, 100).mean()
        department_scores.append(high_threat_dept)
        importance_tags = [5, 5, 5, 5, 1]
        agg_score = calcuaggred(department_scores, importance_tags)
        self.assertTrue(0 <= agg_score <= 90)

    def testcasevariance(self):
        department_scores = [genrandate(40, 20, 10).mean(), 
                             genrandate(30, 10, 150).mean(),
                             genrandate(50, 15, 100).mean(),
                             genrandate(20, 5, 200).mean(),
                             genrandate(35, 10, 50).mean()]
        importance_tags = [3, 2, 4, 1, 5]
        agg_score = calcuaggred(department_scores, importance_tags)
        self.assertTrue(0 <= agg_score <= 90)

    def testcaseoutliers(self):
        department_scores = [genrandate(30, 10, 50).mean(),
                             genrandate(40, 10, 50).mean(),
                             genrandate(90, 0, 10).mean(),
                             genrandate(20, 5, 100).mean(),
                             genrandate(50, 15, 70).mean()]
        importance_tags = [3, 2, 5, 1, 4]
        agg_score = calcuaggred(department_scores, importance_tags)
        self.assertTrue(0 <= agg_score <= 90)

if __name__ == "__main__":
    unittest.main()
