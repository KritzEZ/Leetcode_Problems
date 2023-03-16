class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        splitPath = path.split('/')
        queue = ["/"]

        for i in range(len(splitPath)):
            if splitPath[i] == u'' or splitPath[i] == ".":
                continue
            
            elif splitPath[i] == "..":
                try:
                    queue.pop(len(queue)-1)
                    if len(queue)>0:
                        queue.pop(len(queue)-1)
                except:
                    continue

            else:
                queue.append(str(splitPath[i]))
                queue.append("/")

            print(queue)

        if not queue:
            queue.append("/")
        elif len(queue)>1 and queue[len(queue)-1] == "/":
            queue.pop(len(queue)-1)

        if queue[0] != "/":
            queue.insert(0, "/")

        ans = "".join(queue)

        return ans