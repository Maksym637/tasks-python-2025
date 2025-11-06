-- Problem description: https://www.hackerrank.com/challenges/binary-search-tree-1/problem
WITH NodeCTE AS (
    SELECT N, P,
        CASE
            WHEN N IN (SELECT DISTINCT P FROM BST) AND P IS NULL THEN "Root"
            WHEN N IN (SELECT DISTINCT P FROM BST) THEN "Inner"
            ELSE "Leaf"
        END AS NodeNaming
    FROM BST
)

SELECT N, NodeNaming FROM NodeCTE
ORDER BY N;
